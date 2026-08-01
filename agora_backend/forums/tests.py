from django.test import TestCase
from forums.models import Forum, Tag

class ForumTestCase(TestCase):
    def test_create_forum(self):
        forum = Forum.objects.create(
            name="Programming",
            slug="programming",
            description="A forum for programming discussions."
        )

        self.assertEqual(forum.name, "Programming")
        self.assertEqual(forum.slug, "programming")
        self.assertEqual(forum.description, "A forum for programming discussions.")

    def test_forum_parent(self):
        programming = Forum.objects.create(
            name="Programming",
            slug="programming",
            description="A forum for programming discussions."
        )

        django = Forum.objects.create(
            name="Django",
            slug="django",
            description="A forum for Django discussions.",
            parent=programming
        )

        self.assertEqual(django.parent, programming)
        self.assertIn(django, programming.children.all())


    def test_create_tag(self):
        tag = Tag.objects.create(
            name="Python",
            slug="python"
        )

        self.assertEqual(tag.name, "Python")
        self.assertEqual(tag.slug, "python")
