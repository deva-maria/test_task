import uuid

import pytest

from config.settings import TEST_DIR_PREFIX
from utils.api_client import DiskClient


@pytest.fixture(scope="session")
def client() -> DiskClient:
    return DiskClient()


@pytest.fixture
def folder_path() -> str:
    return f"disk:/{TEST_DIR_PREFIX}_{uuid.uuid4().hex[:8]}"


@pytest.fixture
def created_folder(client: DiskClient, folder_path: str) -> str:
    response = client.create_folder(folder_path)
    assert response.status_code in (201, 409), (
        f"Не получилось создать папку {folder_path}. "
        f"Код: {response.status_code}. Ответ: {response.text}"
    )
    yield folder_path

    delete_response = client.delete_resource(folder_path, permanently=True)
    assert delete_response.status_code in (204, 202, 404), (
        f"Не получилось удалить папку {folder_path} после теста. "
        f"Код: {delete_response.status_code}. Ответ: {delete_response.text}"
    )
