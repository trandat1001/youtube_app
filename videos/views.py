from django.shortcuts import render, redirect
from videos.models import Video
from videos.forms import  VideoForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls  import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

#class VideoListView(ListView):
#    model = Video
#    # The default view is:videos/templates/videos/video_list.html

def index(request):
    videos = Video.objects.all();

    return render(request, "videos/video_list.html",{"videos": videos})

'''class VideoThumbsView(ListView):
    model = Video
    template_name = "videos/video_thumbs.html"

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        result = []
        if (category_id > 0):
            result = Video.objects.filter(category_id=self.kwargs['category_id']).filter(is_active = True)
        else:
            result = Video.objects.all().filter(is_active = True)

        return result
'''
def thumbs(request, category_id):
    videos = []
    if (category_id > 0):
        videos = Video.objects.filter(category_id=category_id).filter(is_active=True)
    else:
        videos = Video.objects.all().filter(is_active=True)

    return render(request, "videos/video_thumbs.html",{"videos": videos})
'''
class VideoDetailView(DetailView):
    model = Video
    # Default assumes videos/templates/videos/video_detail.html
    def get_object(self, queryset=None):
        id = self.kwargs['id']

        return Video.objects.get(pk = id)
'''

def detail(request, id):
    video = Video.objects.get(id = id)

    return render(request, "videos/video_detail.html", {"video": video})


'''class VideoCreateView(SuccessMessageMixin, CreateView):
    model = Video
    fields = ['title', 'author', 'description', 'youtube_vid', 'stars_count', 'category_id', 'skill_level_id', 'is_active']
    # Default assumes videos/templates/videos/video_form.html exist
    success_message = "Video Added!"
    success_url = reverse_lazy('video-list')
'''
def create(request):
    form = VideoForm()

    if request.method == "POST":
        form.setData(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Video Added!')
            return redirect("video-list")
        else:
            print(form.errors)

    return render(request, "videos/video_form.html", {"form": form})

'''class VideoUpdateView(SuccessMessageMixin, UpdateView):
    model = Video
    fields = ['title', 'author', 'description', 'youtube_vid', 'stars_count', 'category_id', 'skill_level_id', 'is_active']
    # Default assumes videos/templates/videos/video_form.html exist
    success_message = "Video Saved!"
    success_url = reverse_lazy('video-list')
'''
def update(request, id):
    video = Video.objects.get(pk = id)
    form = VideoForm(instance=video)

    if request.method == "POST":
        form.setData(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Video Saved!')
            return redirect("video-list")
        else:
            print(form.errors)

    return render(request, "videos/video_form.html", {"form": form})

'''class VideoDeleteView(SuccessMessageMixin, DeleteView):
    model = Video
    # Default assumes videos/templates/videos/video_confirm_delete.html exist
    success_message = "Video Deleted!"
    success_url = reverse_lazy('video-list')
'''
def delete(request, id):
    video = Video.objects.get(pk=id)

    if request.method == "POST":
        video.delete()
        messages.success(request, 'Video Deleted!')
        return redirect("video-list")

    return render(request, "videos/video_confirm_delete.html")