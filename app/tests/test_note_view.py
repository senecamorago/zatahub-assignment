import pytest
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse


@pytest.mark.django_db
class TestNoteView:
    url = reverse("note-view")

    def test_post_a_note_success(self):
        # TODO: Do this unit test for the API here
        client = APIClient()
        response = client.post(self.url)
        assert response.status_code == status.HTTP_201_CREATED
