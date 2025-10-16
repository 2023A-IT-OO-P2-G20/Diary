from diaries.AbstractDiary import AbstractDiary

class NishidaDiary(AbstractDiary):
    def get_date(self):
        return "2025-10-16"
    def get_summary(self):
        return "今日美容院いく！"
    def get_author(self):
        return "西田"