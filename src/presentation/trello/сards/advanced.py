import logging


from presentation.trello.сards.base import CardOperation


class StoryPointOperation(CardOperation):
    def all_calculate(todo_id, in_progress_id, code_review_id,
                      in_test_id, release_id, done_id, token, key):
        try:
            time_todo_list = (CardOperation(todo_id, token, key).
                              get_sum_of_cards())
            time_in_progress_list = (CardOperation(in_progress_id, token, key).
                                     get_sum_of_cards())
            time_code_review_list = (CardOperation(code_review_id, token, key).
                                     get_sum_of_cards())
            time_in_test_list = (CardOperation(in_test_id, token, key).
                                 get_sum_of_cards())
            time_release_list = (CardOperation(release_id, token, key).
                                 get_sum_of_cards())
            time_done_list = (CardOperation(done_id, token, key).
                              get_sum_of_cards())

            total_time = (
                    time_todo_list +
                    time_in_progress_list +
                    time_code_review_list +
                    time_in_test_list +
                    time_release_list +
                    time_done_list
            )
            return total_time
        except IndexError:
            logging.basicConfig(filename="../main/log/exception.log", filemode="w")
            logging.error("Don't have time on card")
            print("Please enter time on card")

    def done_calculate(list_id, token, key):
        try:
            time_done_list = (CardOperation(list_id, token, key).
                              get_sum_of_cards())
            return time_done_list
        except IndexError:
            logging.basicConfig(filename="../main/log/exception.log", filemode="w")
            logging.error("Don't have time on card")
            print("Please enter time on card")

    def release_calculate(list_id, token, key):
        try:
            time_release_list = (CardOperation(list_id, token, key).
                                 get_sum_of_cards())
            return time_release_list
        except IndexError:
            logging.basicConfig(filename="../main/log/exception.log", filemode="w")
            logging.error("Don't have time on card")
            print("Please enter time on card")
