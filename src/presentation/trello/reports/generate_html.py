from presentation.trello.сards.base import CardOperation
from presentation.trello.lists.base import ListOperation
from presentation.trello.сards.advanced import StoryPointOperation
from presentation.trello.boards.base import BoardOperation


class ReportTool():
    def __init__(self, list_id, token, key):
        self.all_cards_on_list = CardOperation(list_id, token, key).get_name_of_card()
        self.list_title = []
        self.list_title.extend([ListOperation.get_name_of_list(list_id, token, key)]
                               * len(self.all_cards_on_list))

    def list_of_cards_with_status(self):
        list_of_cards_with_status = []
        for i in range(len(self.all_cards_on_list)):
            card_name = self.all_cards_on_list[i]
            card_status = self.list_title[i]
            if card_status == "DONE":
                card_with_status = f"<li><strong>{card_name}</strong> " \
                                   f"<span class='card-label card-label-black mod-card-detail-green'> " \
                                   f"<span class='label-text'>{card_status}</span></span></li>"
            else:
                card_with_status = f"<li><strong>{card_name}</strong> " \
                                   f"<span class='card-label card-label-black mod-card-detail-orange'>" \
                                   f"<span class='label-text'>{card_status}</span></span></li>"
            list_of_cards_with_status.append(card_with_status)
        return list_of_cards_with_status


class Category(ReportTool):
    def unfinished(todo_id,
                   in_progress_id,
                   code_review_id,
                   in_test_id,
                   token,
                   key):
        split_cards_in_todo_list = "\n\t\t\t\t".join(ReportTool(
            todo_id, token, key).list_of_cards_with_status())
        split_cards_in_progress_list = "\n\t\t\t\t".join(ReportTool(
            in_progress_id, token, key).list_of_cards_with_status())
        split_cards_in_code_review = "\n\t\t\t\t".join(ReportTool(
            code_review_id, token, key).list_of_cards_with_status())
        split_cards_in_test_list = "\n\t\t\t\t".join(ReportTool(
            in_test_id, token, key).list_of_cards_with_status())

        cards_in_first_category = f"<h1 class='top-indent'> What we don't do: </h1>" \
                                  f"{split_cards_in_todo_list}" \
                                  f"{split_cards_in_progress_list}" \
                                  f"{split_cards_in_code_review}" \
                                  f"{split_cards_in_test_list}"
        return cards_in_first_category

    def task_in_release(release_id,
                        token,
                        key):
        split_cards_in_release_list = "\n\t\t\t\t".join(ReportTool(
            release_id, token, key).list_of_cards_with_status())
        cards_in_second_category = f"<h1 class ='top-indent'>Task in release: </h1>" \
                                   f"{split_cards_in_release_list}"
        return cards_in_second_category

    def complited(list_id, token, key):
        split_cards_in_done_list = "\n\t\t\t\t".join(ReportTool(
            list_id, token, key).list_of_cards_with_status())
        cards_in_third_category = f"<h1 class='top-indent'>What we done: </h1>" \
                                  f"{split_cards_in_done_list}"
        return cards_in_third_category

    def count_story_points_by_categories(todo_id, in_progress_id, code_review_id,
                                         in_test_id, release_id, done_id, token, key):
        count_all_and_done_story_points = ("<h1 class='top-indent'>Total time: </h1>"
                                           "<li><strong>Summary:"
                                           + str(StoryPointOperation.all_calculate(todo_id, in_progress_id,
                                                                                    code_review_id,
                                                                                    in_test_id, release_id, done_id,
                                                                                    token, key)) + "/ "
                                           f"{StoryPointOperation.done_calculate(done_id, token, key)}"
                                           "(All time/Done)</strong></li>"
                                           "<li><strong>Waiting for deploy:"
                                           f"{StoryPointOperation.release_calculate(release_id, token, key)}</strong></li>")
        return count_all_and_done_story_points

    def sprint_name(list_id, token, key):
        board_name = ""f"<h1 class='top-indent'>" \
                     f"{BoardOperation.get_name_of_board(list_id, token, key)}</h1>"
        return board_name
