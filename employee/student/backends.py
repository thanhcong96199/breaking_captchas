from django.contrib.auth.backends import ModelBackend

from student.models import Student




class AuthStudentBackend(ModelBackend):
    def authenticate(self, request, email_student=None, password_student=None, **kwargs):
        if email_student and password_student:
            email = email_student
            password = password_student
        else:
            return None

        try:
            student = Student.objects.get(email=email)
        except Student.DoesNotExist:
            raise Exception("Email or Password wrong")
        if not student.check_password(password):
            raise Exception("Email or Password wrong")
        if not self.user_can_authenticate(student):
            raise Exception("Email or Password wrong")
        return student

    def get_user(self, user_id):
        try:
            return Student.objects.get(pk=user_id)
        except Student.DoesNotExist:
            return None
