from django.test import TestCase

from accounts.models import User
from forums.models import Forum, Tag
from content.models import (
    Content,
    Post,
    Comment,
    Discussion,
    Question,
    Answer
)

class ContentTestCase(TestCase):
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
        self.tag = Tag.objects.create(
            name="Python",
            slug="python"
        )

    def test_create_content(self):
        content = Content.objects.create(
            author=self.user,
            forum=self.forum,
        )

        self.assertEqual(content.author, self.user)
        self.assertEqual(content.forum, self.forum)
        self.assertEqual(
            content.state,
            Content.State.PUBLISHED
        )

    def test_create_post(self):
        content = Content.objects.create(
            author=self.user,
            forum=self.forum,
        )

        post = Post.objects.create(
            content=content,
            title="My First Post",
            body="This is the body of my first post."
        )

        self.assertEqual(post.content, content)
        self.assertEqual(content.post, post)
        self.assertEqual(post.title, "My First Post")
        self.assertEqual(post.body, "This is the body of my first post.")

    def test_content_tags(self):
        content = Content.objects.create(
            author=self.user,
            forum=self.forum,
        )

        post = Post.objects.create(
            content=content,
            title="Python",
            body="Testing tags.",
        )

        content.tags.add(self.tag)

        self.assertIn(self.tag, content.tags.all())
        self.assertIn(content, self.tag.contents.all())

    def test_create_comment(self):
        post_content = Content.objects.create(
            author=self.user,
            forum=self.forum
        )

        Post.objects.create(
            content=post_content,
            title="My First Post",
            body="This is the body of my first post."
        )

        comment_content = Content.objects.create(
            author=self.user,
            forum=self.forum
        )

        comment = Comment.objects.create(
            content=comment_content,
            target=post_content,
            body="This is a comment."
        )

        self.assertEqual(comment.content, comment_content)
        self.assertEqual(comment.target, post_content)

        self.assertIn(
            comment,
            post_content.comments.all()
        )

    def test_nested_comments(self):
        post_content = Content.objects.create(
            author=self.user,
            forum=self.forum,
        )

        Post.objects.create(
            content=post_content,
            title="Post",
            body="Content",
        )

        parent_content = Content.objects.create(
            author=self.user,
            forum=self.forum,
        )

        parent = Comment.objects.create(
            content=parent_content,
            target=post_content,
            body="Comment.",
        )

        reply_content = Content.objects.create(
            author=self.user,
            forum=self.forum,
        )

        reply = Comment.objects.create(
            content=reply_content,
            target=post_content,
            parent=parent,
            body="Answer.",
        )

        self.assertEqual(reply.parent, parent)
        self.assertIn(reply, parent.replies.all())

    def test_discussion_question_answer(self):
        discussion_content = Content.objects.create(
            author=self.user,
            forum=self.forum,
        )

        discussion = Discussion.objects.create(
            content=discussion_content,
            title="What do you think about Django?",
        )

        question_content = Content.objects.create(
            author=self.user,
            forum=self.forum,
        )

        question = Question.objects.create(
            content=question_content,
            discussion=discussion,
            title="Is it good for APIs?",
            body="I want to know some opinions",
        )

        answer_content = Content.objects.create(
            author=self.user,
            forum=self.forum,
        )

        answer = Answer.objects.create(
            content=answer_content,
            question=question,
            body="Yes, specially with DRF.",
        )

        self.assertIn(
            question,
            discussion.questions.all(),
        )

        self.assertIn(
            answer,
            question.answers.all(),
        )
