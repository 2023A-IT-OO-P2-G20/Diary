from diaries.DiarySample import DiarySample
from diaries.HabaDiary import HabaDiary
from diaries.IshimaruDiary import IshimaruDiary
from diaries.taumaDiary import taumaDiary
from diaries.NishidaDiary import NishidaDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(), HabaDiary()] 
# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(), IshimaruDiary()]
# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(), taumaDiary()]
# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(), NishidaDiary()]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()