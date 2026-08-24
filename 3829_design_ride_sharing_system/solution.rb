# LeetCode 3829 - Design Ride Sharing System
# https://leetcode.com/problems/design-ride-sharing-system/

class RideSharingSystem
  def initialize
    @t = 0
    @riders = {}
    @drivers = {}
    @d = {}
    @rider_keys = []
    @driver_keys = []
  end

  def add_rider(rider_id)
    @d[rider_id] = @t
    @riders[@t] = rider_id
    @rider_keys << @t
    @t += 1
    nil
  end

  def add_driver(driver_id)
    @drivers[@t] = driver_id
    @driver_keys << @t
    @t += 1
    nil
  end

  def match_driver_with_rider
    @rider_keys.shift while !@rider_keys.empty? && !@riders.key?(@rider_keys[0])
    @driver_keys.shift while !@driver_keys.empty? && !@drivers.key?(@driver_keys[0])
    return [-1, -1] if @rider_keys.empty? || @driver_keys.empty?
    d_key = @driver_keys.shift
    r_key = @rider_keys.shift
    driver_id = @drivers.delete(d_key)
    rider_id = @riders.delete(r_key)
    [driver_id, rider_id]
  end

  def cancel_rider(rider_id)
    return nil unless @d.key?(rider_id)
    @riders.delete(@d[rider_id])
    nil
  end
end
