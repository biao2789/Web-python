from rest_framework import serializers
from polls.models import Question, Choice


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question_text', 'pub_date', 'choices')
        depth = 1


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id', 'choice_text', 'votes')


class VoteSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        # instance.votes = validated_data.get('votes', instance.votes)
        instance.votes = instance.votes + 1
        instance.save()
        return instance
