from .. import db


class VerseModel(db.Model):

    __tablename__ = 'verses'

    id = db.Column(db.Integer, primary_key=True)
    verse_number = db.Column(db.String)
    text = db.Column(db.String)
    transliteration = db.Column(db.String)
    word_meanings = db.Column(db.String)
    verse_order = db.Column(db.Integer)
    meaning = db.Column(db.String)
    meaning_large = db.Column(db.String)

    chapter_number = db.Column(db.Integer,
                               db.ForeignKey('chapters.chapter_number'))
    chapters = db.relationship('ChapterModel')

    def __init__(self, chapter_number, verse_number, text, transliteration,
                 word_meanings, meaning, verse_order, meaning_large):
        self.chapter_number = chapter_number
        self.verse_number = verse_number
        self.text = text
        self.transliteration = transliteration
        self.word_meanings = word_meanings
        self.meaning = meaning
        self.verse_order = verse_order
        self.meaning_large = meaning_large

    def json(self):
        return {
            'chapter_number': self.chapter_number,
            'verse_number': self.verse_number,
            'text': self.text,
            'transliteration': self.transliteration,
            'word_meanings': self.word_meanings
        }

    @classmethod
    def find_by_verse_number(cls, verse_number):
        return cls.query.filter_by(verse_number=verse_number).first()

    @classmethod
    def find_by_chapter_number_verse_number(cls, chapter_number, verse_number):
        return cls.query.filter_by(
            chapter_number=chapter_number, verse_number=verse_number).first()


class VerseModelHindi(db.Model):

    __tablename__ = 'verses_hi'

    id = db.Column(db.Integer, primary_key=True)
    verse_number = db.Column(db.String)
    word_meanings = db.Column(db.String)
    verse_order = db.Column(db.Integer)
    meaning = db.Column(db.String)
    meaning_large = db.Column(db.String)

    chapter_number = db.Column(db.Integer,
                               db.ForeignKey('chapters.chapter_number'))
    chapters = db.relationship('ChapterModel')

    def __init__(self, chapter_number, verse_number, word_meanings, meaning, verse_order, meaning_large):
        self.chapter_number = chapter_number
        self.verse_number = verse_number
        self.word_meanings = word_meanings
        self.meaning = meaning
        self.verse_order = verse_order
        self.meaning_large = meaning_large


class UserReadingPlanItems(db.Model):

    __tablename__ = 'user_reading_plan_items'

    user_reading_plan_items_id = db.Column(db.Integer, primary_key=True)
    user_reading_plan_id = db.Column(db.String)
    timestamp = db.Column(db.TIMESTAMP())
    chapter_number = db.Column(db.Integer)
    verse_number = db.Column(db.String)
    status = db.Column(db.String)
    batch_id = db.Column(db.String)

    def __init__(self, user_reading_plan_id, timestamp, chapter_number, verse_number, status, batch_id):
        self.user_reading_plan_id = user_reading_plan_id
        self.timestamp = timestamp
        self.chapter_number = chapter_number
        self.verse_number = verse_number
        self.status = status
        self.batch_id = batch_id
