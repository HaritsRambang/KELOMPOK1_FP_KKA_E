import random

def testinput():
    numJobs = int(input("Masukkan jumlah pekerjaan: "))
    numWorkers = int(input("Masukkan jumlah pekerja: "))
    workers = []
    for i in range(numWorkers):
        workerName = input(f"Masukkan nama pekerja ke-{i+1}: ")
        workers.append(workerName)    
    jobTimes = {worker: [] for worker in workers}
    for worker in workers:
        print(f"Masukkan waktu untuk pekerja {worker}:")
        for j in range(numJobs):
            time = int(input(f"Waktu pekerja {worker} untuk pekerjaan {j+1}: "))
            jobTimes[worker].append(time)
    return workers, jobTimes, numJobs

def totalTime(tasks, jobTimes, workers):
    workerTimes = {worker: 0 for worker in workers}
    for job, worker in tasks:
        workerIndex = workers.index(worker)
        workerTimes[worker] += jobTimes[worker][job]
    return max(workerTimes.values())

def getNeighbors(tasks, workers, numJobs):
    neighbors = []
    for i in range(len(tasks)):
        for worker in workers:
            newtasks = tasks[:]
            newtasks[i] = (tasks[i][0], worker)
            neighbors.append(newtasks)
    return neighbors

def hillClimbing(workers, jobTimes, numJobs):
    jobs = list(range(numJobs))
    tasks = [(job, random.choice(workers)) for job in jobs]
    currentTime = totalTime(tasks, jobTimes, workers)
    currentSolution = tasks
    while True:
        neighbors = getNeighbors(currentSolution, workers, numJobs)
        nextSolution = None
        nextTime = currentTime
        for neighbor in neighbors:
            neighborTime = totalTime(neighbor, jobTimes, workers)
            if neighborTime < nextTime:
                nextSolution = neighbor
                nextTime = neighborTime
        if nextSolution is None:
            break
        currentSolution = nextSolution
        currentTime = nextTime
    return currentSolution, currentTime
workers, jobTimes, numJobs = testinput()
solution, totalTime = hillClimbing(workers, jobTimes, numJobs)
print("\nWaktu optimal pekerjaan kepada pekerja:")
for job, worker in solution:
    print(f"Pekerjaan {job+1} diselesaikan pekerja {worker} dalam waktu {jobTimes[worker][job]} jam.")
print(f"Total waktu yang dibutuhkan: {totalTime} jam.")
