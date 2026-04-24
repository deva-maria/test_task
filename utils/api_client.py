import requests

from config.settings import BASE_URL, TOKEN


class DiskClient:
    def __init__(self, token: str = TOKEN, base_url: str = BASE_URL):
        if not token:
            raise ValueError("Токен не добавлен. Необходимо добавить YADISK_TOKEN в .env")

        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": f"OAuth {token}",
                "Accept": "application/json",
            }
        )

# Метод GET
    def get_disk_info(self) -> requests.Response:
        return self.session.get(f"{self.base_url}/v1/disk/")

    def get_resource(self, path: str) -> requests.Response:
        return self.session.get(
            f"{self.base_url}/v1/disk/resources",
            params={"path": path},
        )

# Метод PUT
    def create_folder(self, path: str) -> requests.Response:
        return self.session.put(
            f"{self.base_url}/v1/disk/resources",
            params={"path": path},
        )

# Метод POST
    def move_resource(self, from_path: str, to_path: str) -> requests.Response:
        return self.session.post(
            f"{self.base_url}/v1/disk/resources/move",
            params={"from": from_path, "path": to_path},
        )

# Метод DELETE
    def delete_resource(self, path: str, permanently: bool = True) -> requests.Response:
        return self.session.delete(
            f"{self.base_url}/v1/disk/resources",
            params={"path": path, "permanently": str(permanently).lower()},
        )
