from django.core.management.base import BaseCommand
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        print('Connecting to MongoDB...')
        client = MongoClient()
        print('Connected to MongoDB.')
        db = client['octofit_db']

        # Test data for users
        users = [
            {"email": "john.doe@example.com", "name": "John Doe", "age": 16},
            {"email": "jane.smith@example.com", "name": "Jane Smith", "age": 17},
        ]
        print('Inserting test data for users...')
        db.users.insert_many(users)
        print('Inserted test data for users.')

        # Test data for teams
        teams = [
            {"name": "Team A", "members": ["john.doe@example.com", "jane.smith@example.com"]},
        ]
        print('Inserting test data for teams...')
        db.teams.insert_many(teams)
        print('Inserted test data for teams.')

        # Test data for activities
        activities = [
            {"user": "john.doe@example.com", "activity": "Running", "duration": 30},
        ]
        print('Inserting test data for activities...')
        db.activity.insert_many(activities)
        print('Inserted test data for activities.')

        # Test data for leaderboard
        leaderboard = [
            {"user": "john.doe@example.com", "points": 100},
        ]
        print('Inserting test data for leaderboard...')
        db.leaderboard.insert_many(leaderboard)
        print('Inserted test data for leaderboard.')

        # Test data for workouts
        workouts = [
            {"name": "Morning Run", "duration": 30},
        ]
        print('Inserting test data for workouts...')
        db.workouts.insert_many(workouts)
        print('Inserted test data for workouts.')

        self.stdout.write(self.style.SUCCESS('Successfully populated the database'))
