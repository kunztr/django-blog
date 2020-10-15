# Generated by Django 3.1.2 on 2020-10-15 18:32

from django.db import migrations
from django.utils import timezone


def populate_db(apps, schema_editor):
    Blog = apps.get_model('blog', 'Blog')
    Comment = apps.get_model('blog', 'Comment')
    post1 = Blog(title="Lose Weight With This One Simple Trick!", author="Scammy McScamface", content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sit amet enim luctus, interdum sapien tincidunt, aliquam elit. Phasellus eget lacus diam. Cras quis aliquam erat, ut rhoncus ligula. Vivamus eu iaculis justo. Suspendisse feugiat, eros rutrum venenatis blandit, nibh purus fermentum mi, id condimentum enim felis ut massa. Nam finibus lobortis efficitur. Donec quis nisi quis nulla tincidunt bibendum vel vitae arcu. Morbi id rhoncus felis. Nullam suscipit diam nunc, eu pulvinar turpis finibus non. Sed diam enim, porttitor mollis neque sed, varius feugiat nibh. In et dolor malesuada, tempor odio ut, sagittis mauris.Sed egestas tortor ex, ut pretium turpis malesuada eget. Donec erat nunc, pharetra sit amet malesuada at, sagittis vitae mi. Suspendisse nec orci elit. Sed fringilla efficitur ligula dignissim aliquam. Vestibulum ultrices at augue quis aliquam. In in libero luctus, maximus erat vulputate, efficitur ipsum. Sed dignissim interdum ornare. Nulla id velit in felis suscipit porttitor. Pellentesque semper tortor lectus, eget bibendum dui laoreet accumsan.",
                 posted=timezone.now())
    post1.save()

    post2 = Blog(title="Why Computer Science is the Best Degree", author="Larry Page", content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum finibus scelerisque egestas. Nulla bibendum ornare urna, ac tempor odio interdum sit amet. Aliquam erat volutpat. Cras placerat est sit amet nunc euismod consectetur. Vestibulum et dictum enim. Aliquam dui sem, mattis sit amet ex nec, vehicula efficitur eros. Proin sollicitudin, nibh vel accumsan pellentesque, libero magna pulvinar sem, sed eleifend turpis mauris sit amet ex. Nunc in fringilla tellus.Sed tristique, ipsum id semper mollis, justo tellus ornare risus, ut mattis felis metus eu purus. Aenean porttitor arcu eget nulla pulvinar, non rhoncus nibh tempus. Donec tempor dui id porttitor ornare. Aliquam luctus iaculis nunc non sollicitudin. Cras sollicitudin vulputate enim vitae vestibulum. Vivamus blandit luctus tincidunt. Maecenas porta nibh non neque bibendum efficitur. Nullam feugiat leo a nibh viverra lobortis. Vestibulum eu diam elit. Fusce a mollis urna.",
                 posted=timezone.now())
    post2.save()

    comment1 = Comment(blog=post2, commenter="Mildred", email="milly@gmail.com", content="I agree. It's the best!", posted=timezone.now())
    comment1.save()

    comment2 = Comment(blog=post2, commenter="Buford", email="buffy@gmail.com", content="I'm more of a business person myself.", posted=timezone.now())
    comment2.save()

    comment3 = Comment(blog=post2, commenter="Gretchen", email="gdot@gmail.com", content="Wow what a great post. Thanks.", posted=timezone.now())
    comment3.save()

    comment4 = Comment(blog=post2, commenter="Bart", email="bsimpson@gmail.com", content="Computer science is cool but i prefer electrical engineering.", posted=timezone.now())
    comment4.save()

    post3 = Blog(title="Top 10 Anime Battles", author="Joe", content="Nunc scelerisque tempus massa, eget pulvinar est venenatis in. Curabitur id diam quis odio tempus interdum a id nibh. Mauris a sodales tellus. Nunc dictum orci sed sem iaculis dapibus. Mauris lacinia arcu nulla. Donec nec velit quis diam dignissim ultricies. Vivamus neque leo, faucibus sit amet porta faucibus, tincidunt sit amet arcu. Pellentesque eget ex diam. Proin sed blandit est.",
                 posted=timezone.now())
    post3.save()

    post4 = Blog(title="Mario Kart Wii Was the Best MarioKart. Change My Mind", author="King Boo", content="orem ipsum dolor sit amet, consectetur adipiscing elit. Aenean vitae blandit mauris, tristique posuere ipsum. Morbi id urna sit amet nunc pulvinar commodo. Praesent non augue ut elit ultricies aliquet quis ut metus. Donec suscipit urna sit amet quam facilisis sagittis. Morbi ipsum mauris, tempor nec metus a, congue pretium neque. Vestibulum vitae feugiat leo, malesuada mollis tellus. Nulla eu venenatis risus. Sed convallis, purus a iaculis fringilla, eros ipsum fringilla dui, eu hendrerit dolor mi et elit. Praesent vitae est mattis, sollicitudin tellus in, efficitur tortor. Suspendisse potenti. Morbi vitae augue arcu. Nunc nec mollis ligula, laoreet facilisis mi. Nunc ultricies nunc id eros varius malesuada a at purus. Etiam nulla leo, rutrum a blandit vel, porta ac enim. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Morbi a tellus tortor. Pellentesque porta dui lobortis, porta dolor et, facilisis ex. Mauris luctus lacus quis nisl scelerisque, at euismod sapien ultricies. Nam nec tellus euismod libero efficitur suscipit. Sed malesuada tristique sollicitudin. Aenean iaculis, lectus molestie pulvinar mollis, nisl mi egestas nibh, et hendrerit odio justo eget sapien. Curabitur condimentum quam sit amet tellus sollicitudin viverra consequat id risus. Interdum et malesuada fames ac ante ipsum.",
                 posted=timezone.now())
    post4.save()

    post5 = Blog(title="Why You Shouldn't Wait Until the Day Before to Start a CS Project: An Essay", author="Tyler Kunz", content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam id viverra sem. In euismod erat eros, et dictum massa tempor a. Pellentesque est lorem, feugiat in elementum at, condimentum vel enim. Pellentesque id lacinia ante. Mauris iaculis nisi eu nisl pharetra, ac malesuada neque sollicitudin. In laoreet rhoncus odio id egestas. In at justo odio. Duis mattis vulputate lorem, vel pulvinar nulla consectetur at. Nam sed iaculis elit, quis molestie risus. Phasellus id nisl a eros tincidunt consectetur. Nunc tristique massa nec nisi faucibus, eu aliquet justo vehicula. Duis sed lectus aliquet, consectetur felis at, fermentum leo. Sed commodo facilisis odio a molestie. Quisque sem lectus, volutpat at.",
                 posted=timezone.now())
    post5.save()

    return


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_db)
    ]


