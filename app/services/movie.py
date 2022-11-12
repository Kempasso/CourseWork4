class MovieService:
    def __init__(self, dao):
        self.dao = dao

    def get_all(self, data):
        if data:
            if status := data.get('status', None):
                status = "year"
            page = data.get("page", None)
            return self.dao.get_all(page, status)
        return self.dao.get_all()

    def get_one(self, movie_id):
        return self.dao.get_one(movie_id)
