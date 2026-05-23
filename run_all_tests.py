import subprocess

# قائمة كل ملفات الاختبار
test_files = [
    "ft_alembic_0.py",
    "ft_alembic_1.py",
    "ft_alembic_2.py",
    "ft_alembic_3.py",
    "ft_alembic_4.py",
    "ft_alembic_5.py",
    "ft_distillation_0.py",
    "ft_distillation_1.py",
    "ft_distillation_2.py",
    "ft_transmutation_0.py",
    "ft_transmutation_1.py",
    "ft_transmutation_2.py",
    "ft_kaboom_0.py",
    "ft_kaboom_1.py"
]

# تشغيل كل ملف وطباعة النتيجة
for file in test_files:
    print(f"\n=== Running {file} ===")
    subprocess.run(["python3", file])