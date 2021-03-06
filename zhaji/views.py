from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from zhaji.models import Category, Book, Note
#from zhaji.forms import CategoryForm, PageForm

def about(request):
    return HttpResponse("This is About Page")

def index(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    category_list = Category.objects.order_by('-likes')[:5]
    book_list = Book.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list, 'books': book_list}

    # Render the response and send it back!
    return render(request, 'zhaji/index.html', context_dict)

def category(request, category_name_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name

        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        books = Book.objects.filter(category=category)

        # Adds our results list to the template context under name pages.
        context_dict['books'] = books
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'zhaji/category.html', context_dict)

def book(request, book_isbn):
    context_dict = {}

    try:
        book = Book.objects.get(isbn=book_isbn)
        context_dict['book'] = book

        notes = Note.objects.filter(book=book)
        context_dict['notes'] = notes
    except Book.DoesNotExist:
        pass

    return render(request, 'zhaji/book.html', context_dict)

def note(request, note_pk):
    context_dict = {}

    try:
        note = Note.objects.get(pk=note_pk)
        context_dict['note'] = note

    except Book.DoesNotExist:
        pass

    return render(request, 'zhaji/note.html', context_dict)

#def add_category(request):
    # A HTTP POST?
#    if request.method == 'POST':
#        form = CategoryForm(request.POST)

        # Have we been provided with a valid form?
#        if form.is_valid():
            # Save the new category to the database.
#            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
#            return index(request)
#        else:
            # The supplied form contained errors - just print them to the terminal.
#            print form.errors
#    else:
        # If the request was not a POST, display the form to enter details.
#        form = CategoryForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
#    return render(request, 'zhaji/add_category.html', {'form': form})

#def add_page(request, category_name_slug):

#    try:
#        cat = Category.objects.get(slug=category_name_slug)
#    except Category.DoesNotExist:
#        cat = None

#    if request.method == 'POST':
#        form = PageForm(request.POST)
#        if form.is_valid():
#            if cat:
#                page = form.save(commit=False)
#                page.category = cat
#                page.views = 0
#                page.save()
                # probably better to use a redirect here.
#                return category(request, category_name_slug)
#        else:
#            print form.errors
#    else:
#        form = PageForm()

#    context_dict = {'form':form, 'category': cat}

#    return render(request, 'zhaji/add_page.html', context_dict)
