from rest_framework import serializers

from ..models import Post, PostScore


class PostScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostScore
        fields = ('score',)

    def create(self, validated_data):
        user = validated_data['user']
        post = validated_data['post']
        obj, created = PostScore.objects.get_or_create(
            user=user,
            post=post,
            defaults={'score': validated_data['score']})
        if created:
            post.score_count += 1
            post.score_sum += obj.score
            post.save()
        else:
            print(obj)
            post.score_sum += validated_data['score'] - obj.score
            post.save()
            obj.score = validated_data['score']
            obj.save()
        return obj


class ListPostSerializer(serializers.ModelSerializer):
    score_average = serializers.FloatField()
    my_score = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('title', 'score_count', 'score_average', 'my_score',)

    def get_my_score(self, obj):
        my_score = PostScore.objects.filter(user=self.context['request'].user, post=obj).first()
        return PostScoreSerializer(my_score).data
