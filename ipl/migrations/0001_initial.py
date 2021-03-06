# Generated by Django 4.0.6 on 2022-07-08 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='matches',
            fields=[
                ('id', models.IntegerField(max_length=10, primary_key=True, serialize=False)),
                ('season', models.IntegerField(max_length=20, null=True)),
                ('city', models.CharField(max_length=200, null=True)),
                ('date', models.CharField(max_length=200, null=True)),
                ('team1', models.CharField(max_length=200, null=True)),
                ('team2', models.CharField(max_length=200, null=True)),
                ('toss_winner', models.CharField(max_length=200, null=True)),
                ('toss_decision', models.CharField(max_length=200, null=True)),
                ('result', models.CharField(max_length=200, null=True)),
                ('dl_applied', models.IntegerField(max_length=200, null=True)),
                ('winner', models.CharField(max_length=200, null=True)),
                ('win_by_runs', models.IntegerField(max_length=200, null=True)),
                ('win_by_wickets', models.IntegerField(max_length=200, null=True)),
                ('player_of_match', models.CharField(max_length=200, null=True)),
                ('venue', models.CharField(max_length=200, null=True)),
                ('umpire1', models.CharField(max_length=200, null=True)),
                ('umpire2', models.CharField(max_length=200, null=True)),
                ('umpire3', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='deliveries',
            fields=[
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ipl.matches')),
                ('inning', models.CharField(max_length=200, null=True)),
                ('batting_team', models.CharField(max_length=200, null=True)),
                ('bowling_team', models.CharField(max_length=200, null=True)),
                ('over', models.IntegerField(max_length=200, null=True)),
                ('ball', models.IntegerField(max_length=200, null=True)),
                ('batsman', models.CharField(max_length=200, null=True)),
                ('non_striker', models.CharField(max_length=200, null=True)),
                ('bowler', models.CharField(max_length=200, null=True)),
                ('is_super_over', models.IntegerField(null=True)),
                ('wide_runs', models.IntegerField(max_length=200, null=True)),
                ('bye_runs', models.IntegerField(max_length=200, null=True)),
                ('legbye_runs', models.IntegerField(max_length=200, null=True)),
                ('noball_runs', models.IntegerField(max_length=200, null=True)),
                ('penalty_runs', models.IntegerField(max_length=200, null=True)),
                ('batsman_runs', models.IntegerField(max_length=200, null=True)),
                ('extra_runs', models.IntegerField(max_length=200, null=True)),
                ('total_runs', models.IntegerField(max_length=200, null=True)),
                ('player_dismissed', models.CharField(max_length=200, null=True)),
                ('dismissal_kind', models.CharField(max_length=200, null=True)),
                ('fielder', models.CharField(max_length=200, null=True)),
                ('id', models.IntegerField(max_length=200, primary_key=True, serialize=False)),
                
            ],
        ),
    ]
