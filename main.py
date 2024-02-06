from lib.LogManager.LogManager import LogManager
from src.MelonTicketReservationManager import MelonTicketReservationManager
import time


def main():
    loger = LogManager()
    manager = MelonTicketReservationManager(loger, 'https://ticket.melon.com/performance/index.htm?prodId=209333')
    manager.test_logic()
    time.sleep(500)
    return


if __name__ == '__main__':
    main()
