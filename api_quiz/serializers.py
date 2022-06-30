from rest_framework import serializers

from accs.models import Quiz, Question


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = (
            "name",
            "uname",
            "res",
            "questions",
            "date_created",
        )

    def validate(self, attrs):
        allowed_values = "123456789"
        raw_answers = list(attrs["res"])
        answers = []
        if not attrs["questions"]:
            for question in Question.objects.all():
                attrs["questions"].append(question)
        for answer in raw_answers:
            if answer in allowed_values:
                answers.append(answer)
        if len(answers) != len(attrs["questions"]):
            raise serializers.ValidationError({"res": "Количество ответов должно быть равным количеству вопросов"})
        return attrs
