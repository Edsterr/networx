import os
import random

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

  fnames = ["George", "Fredrick", "Taylor", "Frank", "Sarah", "Andrea", "Mercedes", "Fay", "Cameron", "Simon", "Delilah", "Barbra", "Jim", "Adam"
            "Otto", "Theodore", "Diedre", "Fabiola", "Cristopher", "Alec", "Betsey", "Alline", "Eve", "Monserrate", "Kasi", "Jenelle", "Casey", "Kristel", "Rob", "Athena"
            "Werner", "Seema", "Terri", "Gloria", "Simona", "Brock", "Hwa", "Meredith", "Charita", "Racheal", "Frankie", "Sook", "Olin", "Warren", "Rhonda", "Chandra"
            "Jeremiah", "Lester", "Porsha", "Daron", "Hyun", "Francina", "Nola", "Felicidad", "Margarite", "Merri", "Kazuko", "Ellamae", "Carleen", "Anabel", "Sal", "Alfredia", "Nieves"]
  lnames = ["Moore", "Smith", "Lautner", "Sinatra", "Simpson", "Reason", "Benz", "McGregor"]
  letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
  locations = ["Glasgow-Alhambra", "Glasgow-Bothwell"]
  # greg = [Skills(skillName="Python", skillLevel="13")]
  users = []
  for i in range(50):
      NAME=(fnames[random.randint(0,len(fnames)-1)]+" "+lnames[random.randint(0,len(lnames)-1)])
      SID=(letters[random.randint(0,25)]+str(random.randint(100000,999999)))
      LOCATION=locations[random.randint(0,1)]
      FLOOR=random.randint(0,7)
      userNet = User(name=NAME, sid=SID,location=LOCATION,floor=FLOOR)
      userNet.save()
      print(userNet.sid)
  # userNet.skills.set(greg)
  #userNet.save()


# Start execution here!
if __name__ == '__main__':
  print("Starting networkx $%$ population script...")
  populate()
