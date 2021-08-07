from django.shortcuts import render, get_object_or_404
from presentation.models import PresentationData
from report.models import Config
from presentation.trello.reports.generate_html import Category
from presentation.trello.boards.base import BoardOperation


def presentation(request, user_id,):
    post = get_object_or_404(Config.objects.filter(user=request.user, pk=user_id))
    unfinished = Category.unfinished(post.todo_id,
                                     post.in_progress_id,
                                     post.code_review_id,
                                     post.in_test_id,
                                     post.token,
                                     post.key,)
    task_in_release = Category.task_in_release(post.release_id,
                                               post.token,
                                               post.key,)
    completed = Category.complited(post.done_id,
                                   post.token,
                                   post.key,)
    story_points = Category.count_story_points_by_categories(post.todo_id,
                                                             post.in_progress_id,
                                                             post.code_review_id,
                                                             post.in_test_id,
                                                             post.release_id,
                                                             post.done_id,
                                                             post.token,
                                                             post.key,)
    board_name = Category.sprint_name(post.board_id,
                                      post.token,
                                      post.key,)

    presentation_name = BoardOperation.get_name_of_board(post.board_id, post.token, post.key )
    data =  PresentationData(
                     presentation_name = presentation_name,
                     unfinished=unfinished,
                     task_in_release=task_in_release,
                     completed=completed,
                     story_points=story_points,
                     board_name=board_name,
                     presentation=post)

    data.save()

    form = PresentationData.objects.all
    context = {
        'form': form
    }

    return render(request, 'generated_presentation.html', context)


def show_all_presentation(request):
    form = PresentationData.objects.all()
    context = {
        'form': form
    }
    return render(request, 'show_all_presentation.html', context)


def sprint_name(request, presentation_id):
    post = PresentationData.objects.get(pk=presentation_id)
    context = {
        'post': post,
    }
    return render(request, 'sprint_name.html', context=context)


def completed(request, presentation_id):
    post = PresentationData.objects.get(pk=presentation_id)
    context = {
        'post': post,
    }
    return render(request, 'completed.html', context=context)


def task_in_release(request, presentation_id):
    post = PresentationData.objects.get(pk=presentation_id)
    context = {
        'post': post,
    }
    return render(request, 'task_in_release.html', context=context)


def unfinished(request, presentation_id):
    post = PresentationData.objects.get(pk=presentation_id)
    context = {
        'post': post,
    }
    return render(request, 'unfinished.html', context=context)


def story_point(request, presentation_id):
    post = PresentationData.objects.get(pk=presentation_id)
    context = {
        'post': post,
    }
    return render(request, 'total_story_points.html', context=context)


def planing_to_do(request, presentation_id):
    post = PresentationData.objects.get(pk=presentation_id)
    context = {
        'post': post,
    }
    return render(request, 'planing_to_do.html', context=context)


def question(request, presentation_id):
    post = PresentationData.objects.get(pk=presentation_id)
    context = {
        'post': post,
    }
    return render(request, 'questions.html', context=context)