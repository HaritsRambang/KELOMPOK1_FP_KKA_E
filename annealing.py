import random
import math

def testInput():
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
        workerTimes[worker] += jobTimes[worker][job]
    return max(workerTimes.values())

def getNeighbor(tasks, workers):
    newTasks = tasks[:]
    job1, job2 = random.sample(range(len(tasks)), 2)
    newTasks[job1], newTasks[job2] = (newTasks[job2][0], tasks[job1][1]), (newTasks[job1][0], tasks[job2][1])
    return newTasks

def simulatedAnnealing(tasks, jobTimes, workers, initialTemperature, coolingRate, maxIterations):
    currentTasks = tasks
    currentTime = totalTime(currentTasks, jobTimes, workers)
    bestTasks = currentTasks
    bestTime = currentTime
    temperature = initialTemperature

    for iteration in range(maxIterations):
        neighborTasks = getNeighbor(currentTasks, workers)
        neighborTime = totalTime(neighborTasks, jobTimes, workers)

        if neighborTime < currentTime or random.random() < math.exp((currentTime - neighborTime) / temperature):
            currentTasks = neighborTasks
            currentTime = neighborTime

        if currentTime < bestTime:
            bestTasks = currentTasks
            bestTime = currentTime

        temperature *= coolingRate

    return bestTasks, bestTime

workers, jobTimes, numJobs = testInput()

tasks = [(job, random.choice(workers)) for job in range(numJobs)]

initialTemperature = 120
coolingRate = 0.75
maxIterations = 120

bestTasks, bestTime = simulatedAnnealing(tasks, jobTimes, workers, initialTemperature, coolingRate, maxIterations)

print("\nPenugasan Pekerjaan Terbaik:")
for job, worker in bestTasks:
    print(f"Pekerjaan {job+1} diselesaikan pekerja {worker} dalam waktu {jobTimes[worker][job]} jam.")
print(f"Total waktu yang dibutuhkan: {bestTime} jam.")
