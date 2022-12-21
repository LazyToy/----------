from imap_tools import MailBox
from account import *

# mailbox = MailBox("imap.gmail.com", 993)
# mailbox.login(EMAIL_ADRESS, EMAIL_PASSWORD, initial_folder="INBOX")

with MailBox("imap.gmail.com", 993).login(EMAIL_ADRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    # for msg in mailbox.fetch(): # 전체 메일 다 가져오기
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # for msg in mailbox.fetch('(UNSEEN)'): # 읽지 않은 메일만 가져오기
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # for msg in mailbox.fetch('(FROM hayeonggim63@gmail.com)', limit=5, reverse=True): # 특정인이 보낸 파일만 조회
    #      print("[{}] {}".format(msg.from_, msg.subject))

    # 작은 따옴표로 먼저 감싸고, 실제 TEXT 부분은 큰 따옴표로 감싸주세요
    # for msg in mailbox.fetch('(TEXT "test mail")', limit=5, reverse=True): # 어떤 글자를 포함하는 메일 (제목, 본문)
    #      print("[{}] {}".format(msg.from_, msg.subject))

    # for msg in mailbox.fetch(limit=5, reverse=True): # 어떤 글자(한글)을 포함하는 메일 필터링
    #     if "테스트" in msg.subject:
    #      print("[{}] {}".format(msg.from_, msg.subject))

    # for msg in mailbox.fetch('(SENTSINCE 07-Nov-2022)', limit=5, reverse=True): # 특정 날자 이후의 메일
    #      print("[{}] {}".format(msg.from_, msg.subject))
         
    #  for msg in mailbox.fetch('(ON 21-Nov-2022)', limit=5, reverse=True): # 특정 날짜에 온 메일
    #      print("[{}] {}".format(msg.from_, msg.subject))

    # 2가지 이상의 조건을 모두 만족하는 메일 (또는 조건)
     for msg in mailbox.fetch('(OR ON 20-Dec-2022 SUBJECT "test mail")', limit=5, reverse=True): # 특정 날짜에 온 메일
         print("[{}] {}".format(msg.from_, msg.subject))
