from django.contrib.auth import get_user_model

def run():
    User = get_user_model()
    if not User.objects.filter(username='admin').exists():
        print("⚙️ Creando superusuario...")
        User.objects.create_superuser('admin', 'admin@example.com', '123')
        print("✅ Superusuario creado.")
    else:
        print("👤 El superusuario ya existe.")











