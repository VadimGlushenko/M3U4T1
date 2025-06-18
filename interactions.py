from users.models import Role, CustomUser

# Створення ролей
admin_role, _ = Role.objects.get_or_create(name='admin')
user_role, _ = Role.objects.get_or_create(name='user')

# Додавання користувача
new_user = CustomUser.objects.create(
    name="Іван Петренко",
    email="ivan@example.com",
    role=user_role
)

# Зміна ролі користувача
user = CustomUser.objects.get(email="ivan@example.com")
user.role = admin_role
user.save()

# Додавання користувача до групи (ролі)
new_admin = CustomUser.objects.create(
    name="Марія Сидорова",
    email="maria@example.com",
    role=admin_role
)

# Виведення всіх користувачів з роллю "admin"
admins = CustomUser.objects.filter(role__name='admin')
print("Адміністратори:")
for user in admins:
    print(f"- {user.name} ({user.email})")