# LeetCode 2254 - Design Video Sharing Platform
# https://leetcode.com/problems/design-video-sharing-platform/

class MinHeap
  def initialize
    @a = []
  end

  def push(x)
    @a << x
    up(@a.length - 1)
  end

  def pop
    top = @a[0]
    last = @a.pop
    unless @a.empty?
      @a[0] = last
      down(0)
    end
    top
  end

  def empty?
    @a.empty?
  end

  private

  def up(i)
    while i > 0
      p = (i - 1) >> 1
      break if @a[i] >= @a[p]

      @a[i], @a[p] = @a[p], @a[i]
      i = p
    end
  end

  def down(i)
    n = @a.length
    loop do
      s = i
      l = i * 2 + 1
      r = l + 1
      s = l if l < n && @a[l] < @a[s]
      s = r if r < n && @a[r] < @a[s]
      break if s == i

      @a[i], @a[s] = @a[s], @a[i]
      i = s
    end
  end
end

class VideoSharingPlatform
  def initialize
    @next_id = 0
    @free = MinHeap.new
    @videos = {}
    @views = {}
    @likes = {}
    @dislikes = {}
  end

  def upload(video)
    vid = if @free.empty?
            id = @next_id
            @next_id += 1
            id
          else
            @free.pop
          end
    @videos[vid] = video
    @views[vid] = 0
    @likes[vid] = 0
    @dislikes[vid] = 0
    vid
  end

  def remove(video_id)
    return nil unless @videos.key?(video_id)

    @videos.delete(video_id)
    @views.delete(video_id)
    @likes.delete(video_id)
    @dislikes.delete(video_id)
    @free.push(video_id)
    nil
  end

  def watch(video_id, start_minute, end_minute)
    v = @videos[video_id]
    return "-1" if v.nil?

    @views[video_id] += 1
    return "" if start_minute >= v.length

    end_minute = [end_minute, v.length - 1].min
    v[start_minute..end_minute]
  end

  def like(video_id)
    @likes[video_id] += 1 if @videos.key?(video_id)
    nil
  end

  def dislike(video_id)
    @dislikes[video_id] += 1 if @videos.key?(video_id)
    nil
  end

  def get_likes_and_dislikes(video_id)
    return [-1] unless @videos.key?(video_id)

    [@likes[video_id], @dislikes[video_id]]
  end

  def get_views(video_id)
    return -1 unless @videos.key?(video_id)

    @views[video_id]
  end
end
