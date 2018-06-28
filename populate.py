import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'networx.settings')
import django

django.setup()
from app.models import User
from app.models import Skills
#from django.contrib.auth.models import User


def populate():
  # clear tables
  User.objects.all().delete()
  # insert supplier values
  greg = Skills(skillName="2", skillLevel="13")
  users = []
  userNet = User(name='Net Worx', sid='W560370', location="Glasgow-Alhambra", floor=4)
  userNet.save()
  #userNet.skills.set(greg)
  #userNet.save()


# Start execution here!
if __name__ == '__main__':
  print("Starting networkx $%$ population script...")
  populate()
