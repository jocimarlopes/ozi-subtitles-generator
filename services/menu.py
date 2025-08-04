import os 

class Menu:
    def __init__(self):
        self.videos_folder = "videos"
        self.subtitles_folder = "subtitles"
        print("\n📼 Ozi - A Subtitles Generator\n")
        print("by Jocimar Lopes (Jolo Systems)\n")

    def _list_videos(self):
        mp4_files = [f for f in os.listdir(self.videos_folder) if f.endswith(".mp4")]
        video_list = []

        for index, video_file in enumerate(mp4_files):
            video_name = os.path.splitext(video_file)[0]
            subtitle_path = os.path.join(self.subtitles_folder, f"{video_name}.srt")
            has_subtitle = os.path.exists(subtitle_path)
            status = "✅ Subtitle found" if has_subtitle else "❌ Subtitle missing"
            print(f"[{index}] {video_file} - {status}")
            video_list.append(video_file)
        return video_list
    
    def get_video_path(self):
        video_list = self._list_videos()
        if not video_list:
            print("❌ No videos found.\nPlease add videos to the 'videos' folder.\n")
            exit(1)
        try:
            index = int(input("\nSelect the index of the video to process: "))
            selected_video = video_list[index]
        except (ValueError, IndexError):
            print("❌ Invalid selection.")
            exit(1)
        video_path = os.path.join(self.videos_folder, selected_video)
        return video_path