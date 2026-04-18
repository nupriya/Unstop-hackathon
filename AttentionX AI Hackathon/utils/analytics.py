import matplotlib.pyplot as plt

def plot_emotional_timeline(segments, scores):
    times = [s["start"] for s in segments]

    plt.figure()
    plt.plot(times, scores)
    plt.title("Emotional / Viral Peaks")
    plt.xlabel("Time")
    plt.ylabel("Score")

    path = "temp/timeline.png"
    plt.savefig(path)
    plt.close()

    return path