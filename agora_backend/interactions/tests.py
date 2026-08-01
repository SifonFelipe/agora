from django.db import IntegrityError
from django.test import TestCase

from accounts.models import User
from forums.models import Forum
from content.models import Content
from interactions.models import Like

class LikeTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="password123",
        )
        self.forum = Forum.objects.create(
            name="Programming",
            slug="programming",
            description="A forum for programming discussions."
        )
        self.content = Content.objects.create(
            author=self.user,
            forum=self.forum,
        )

    def test_user_can_like_content(self):
        like = Like.objects.create(
            user=self.user,
            content=self.content,
        )

        self.assertEqual(like.user, self.user)
        self.assertEqual(like.content, self.content)
        self.assertEqual(self.content.likes.count(), 1)

    def test_user_cannot_like_same_content_twice(self):
        Like.objects.create(
            user=self.user,
            content=self.content,
        )

        with self.assertRaises(IntegrityError):
            Like.objects.create(
                user=self.user,
                content=self.content,
            )
