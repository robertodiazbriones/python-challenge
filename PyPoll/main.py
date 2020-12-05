import csv

filename='Resources/election_data.csv'

#Rewading File
with open(filename) as f:
    reader = csv.reader(f)
    header_row =next(reader)

#Initializing variables    
    i=0
    total_votes=0
    candidates=[]
    list_candidates=[]
    votes_candidates=[]
    votes_percentage=[]
    candidates_votes={}
    
#Extract Canididates column data
    for row in reader:
        total_votes+=1
        candidates.append(row[2])
    
#Extract Candidates
    for candidate in candidates:
        if candidate not in list_candidates:
           list_candidates.append(candidate)
    
#Extract votes for each candidate
    for candidate in list_candidates:
        votes=candidates.count(candidate)
        votes_candidates.append(votes)
    
#Get Percentage
    for votes in votes_candidates:
        percentage=round((votes/total_votes * 100),3)
        votes_percentage.append(percentage)
        
#Create dictionary with candidates votes

    for key in list_candidates:
        for value in votes_candidates:
            candidates_votes[key]=value
            
#Printing Results 
    print("Election Results")
    print("------------------")   
    print("Total votes: "+str(total_votes))
    print("------------------")
    for candidate in list_candidates:
        prompt=str(list_candidates[i])+":"+ str(votes_percentage[i])
        prompt+="% ("+str(votes_candidates[i])+")"
        print(prompt)
        i+=1
    print("------------------")
    print("Winner: "+max(candidates_votes, key=candidates_votes.get))
    print("------------------")
    
#Create Results file to export results
    i=0    
    ResultsFile=open("analysis/Election_Results.txt", "w")  
    ResultsFile.write("Election Results\n")
    ResultsFile.write("------------------\n")   
    ResultsFile.write("Total votes: "+str(total_votes)+"\n")
    ResultsFile.write("------------------\n")
    for candidate in list_candidates:
        prompt=str(list_candidates[i])+":"+ str(votes_percentage[i])
        prompt+="% ("+str(votes_candidates[i])+")\n"
        ResultsFile.write(prompt)
        i+=1
    ResultsFile.write("------------------\n")
    ResultsFile.write("Winner: "+max(candidates_votes, key=candidates_votes.get)+"\n")
    ResultsFile.write("------------------\n")  
    ResultsFile.close()        
            