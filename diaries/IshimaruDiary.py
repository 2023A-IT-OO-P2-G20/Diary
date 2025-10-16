from diaries.AbstractDiary import AbstractDiary

class IshimaruDiary(AbstractDiary):
    def get_date(self):
        return "2025-10-16"
    def get_summary(self):
        return "gitの練習をした"
    def get_author(self):
        return "Ishimaru"