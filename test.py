import logging
import logging.handlers
import sys

logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
# logger instance 생성
logger = logging.getLogger(__name__)

# logger formatter 설정
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')

# handler 생성 (stream, file)
streamHandler = logging.StreamHandler()
fileHandler = logging.FileHandler('./test.log')

# logger instance 에 formatter 설정
streamHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)

# logger instance 에 handler 설정
logger.addHandler(streamHandler)
logger.addHandler(fileHandler)


a = ['ㄱ', 'ㄴ', 'ㄷ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅅ', 'ㅇ', 'ㅈ', 'ㅊ']
b = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

test = [(a[n] + b[n]) for n in range(10)]
# print(test)

# 해당하는 수준의 로그만 보여줌. 밑으로 갈수록 치명적인 log
logger.debug(f'수준 :  {test}')
logger.info(f'수준 : {test}')
logger.warning(f'수준 : {test}')
logger.error(f'수준 : {test}')
logger.critical(f'수준 : {test}')

