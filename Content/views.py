from django.shortcuts import render
from .forms import CreateContentView, CreateComment
from .models import BookModel, CommentModel
from Account.models import User


def CreateBook(request):
    if request.method == 'POST':
        book_form = request.POST
        header = book_form.getlist('Head')[0]
        Stext = book_form.getlist('ShortText')[0]
        NewBook = BookModel(user_id=request.session['ID'],
                            ShortText=Stext,
                            Header=header,
                            Rating=0,
                            Author=request.session['NickName'],
                            AuthorURL=request.session['URL'])
        NewBook.save()
        return render(request, "Content/success.html", {'URL': NewBook.get_absolute_url()})
    else:
        Idea_form = CreateContentView()
        return render(request, "Content/Create.html", {'form': Idea_form})


def BookView(request, ID_Book, ID_User):
    if request.method == 'POST':
        form = request.POST
        DataList = list(form)
        if 'CommentField' in DataList:
            Text = form.getlist('CommentField')[0]
            Book = BookModel.objects.get(book_id=ID_Book)
            CurUser = User.objects.get(user_id=request.session['ID'])
            NewComment = CommentModel(Text=Text,
                                      UserURL=CurUser.get_absolute_url(),
                                      UserNickName=CurUser.NickName,
                                      book_id=Book.book_id,
                                      user_id=CurUser.user_id)
            NewComment.save()
            DataBook = {'header': Book.Header, 'ShortText': Book.ShortText, 'Rating': Book.Rating}
            DataComment = CommentModel.objects.filter(book_id=ID_Book)
            Comment_form = CreateComment()
            return render(request, "Book/base.html", {'DataBook': DataBook,
                                                      'Comment': Comment_form,
                                                      'DataComment': DataComment})
    else:
        Book = BookModel.objects.get(book_id=ID_Book)
        data = {'header': Book.Header,'ShortText':Book.ShortText,'Rating':Book.Rating}
        DataComment = CommentModel.objects.filter(book_id=ID_Book)
        Comment_form = CreateComment()
        return render(request, "Book/base.html", {'DataBook': data,
                                                  'Comment': Comment_form,
                                                  'DataComment': DataComment})
# Create your views here.
