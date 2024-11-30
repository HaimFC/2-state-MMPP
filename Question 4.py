import numpy as np
import matplotlib.pyplot as plt
import math


def runMMPP(B, r):
    # Parameters
    on_rate = r / B  # Average time spent in the "on" state (lambda for exponential distribution)
    off_rate = 1 - r / B  # Average time spent in the "off" state
    burst_rate = B  # Rate of event generation in the "on" state (bursty)
    total_time = 500  # Total time for the simulation

    # Time tracking and event list
    time = 0
    events = []
    total_events = 0  # Total number of events generated
    on_times = []  # Store "on" times for burst averaging
    off_times = []
    queue = 0
    queueOccupucy = []
    queueOccupucy.append(queue)

    # Simulate Markov process
    while time < total_time:
        # Time in "on" state
        on_time = np.random.exponential(on_rate)
        time += on_time
        if time > total_time:
            break

        on_times.append(on_time)

        # Generate bursty events during "on" state
        burst_events = np.random.poisson(burst_rate * on_time)
        total_events += burst_events
        events.append((time, burst_events))
        queue += burst_events  # for the occupacy
        # send one packet each time slot if ON
        temp_queue = queue
        for i in range(math.floor(on_time)):
            temp_queue -= 1
            queueOccupucy.append(temp_queue)
        queue -= math.floor(on_time)  # more general

        # Time in "off" state
        off_time = np.random.exponential(off_rate)
        off_times.append(off_time)

        time += off_time
        if time > total_time:
            break
        for i in range(math.ceil(off_time)):
            queueOccupucy.append(temp_queue)

        # No events generated during "off" state
        events.append((time, 0))

    # Extract times and events for plotting
    times, num_events = zip(*events)

    # Calculate the overall rate (total events / total time including off periods)
    overall_rate = total_events / total_time

    # Calculate the average burst size (total events / total "on" time)
    total_on_time = sum(on_times)
    average_burst = total_events / total_on_time

    # Print the calculated values
    print(f"Overall event rate (including off periods): {overall_rate:.2f} events per unit time")
    print(f"Average burst size (in 'on' state): {average_burst:.2f} events per unit on-time")

    ticksEvents = [0] * 100
    temp_max = 0
    intervals_begin = 0
    intervals_end = 5
    index = 0

    # Loop through events to collect the max of every 5
    for event_count in events:
        # Every 5th tick, append the max to the list
        if event_count[0] < intervals_end and event_count[0] >= intervals_begin:
            # Update the max within each 5 time slots
            num = event_count[1]
            if num > temp_max:
                temp_max = num
        else:
            if (index > 99):
                break
            ticksEvents[index] = temp_max
            index += 1
            temp_max = 0  # Reset for the next 5 slots
            intervals_begin += 5
            intervals_end += 5

    print(f"len ticks",len(ticksEvents))

    fig = plt.figure()
    fig.suptitle('Maximum Packets in Queue every Tick with rate:' + str(r) + 'and Burst:' + str(B))
    plt.bar(np.arange(total_time / 5), ticksEvents)  # needs to be changed to 100 ticks
    plt.xlabel('Ticks (each tick is 5 time slots)')
    plt.ylabel('Number of packets in Queue')
    plt.show()

    print("on times:")
    print(on_times)
    print("off times")
    print(off_times)
    print("events")
    print(events)


runMMPP(20, 1)
runMMPP(3, 1.5)