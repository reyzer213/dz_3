import django_setup

from some.models import Member, Screening, Movie


movie1 = Movie(
    name='Peaky Blinders',
    date='2013-01-01',
    director='Stiven',
    genre='criminal'
)
movie1.save()


movie_to_update = Movie.objects.get(id=movie1.id)
print(movie_to_update.name)
movie_to_update.director = 'Bodya'
movie_to_update.save()


movie_to_update = Movie.objects.get(id=movie1.id)
print(movie_to_update.name)
movie_to_update.director = 'Bodya'
movie_to_update.save()


member1 = Member(
    name='Bogdan',
    second_name='Petrov',
    email='gargach@gmail.com'
)
member1.save()


delete_member1 = Member.objects.get(id=member1.id)
delete_member1.delete()


update_member1 = Member.objects.get(id=member1.id)
update_member1.name = 'Arthur'
update_member1.save()


screening1 = Screening(
    film=movie_to_update,
    date='2015-01-01',
    place='Southampton'
)
screening1.save()
screening1.members.set([member1, member1])
screening1.save()


update_screening1 = Screening.objects.get(id=screening1.id)
update_screening1.place = 'Kyiw'
update_screening1.save()


screening1.delete()


while True:
    print("Введіть ім'я нового учасника: ")
    str1 = input()
    print("Введіть прізвище нового учасника: ")
    str2 = input()
    print("Введіть email нового учасника: ")
    str3 = input()
    new_member = Member(name=str1, second_name=str2, email=str3)
    new_member.save()
