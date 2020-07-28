	gsize_percentages=[]
	labels=[]
	for gsize in genome_sizes:
		labels.append(label_map[gsize][:-1])
		maps = sorted([f for f in os.listdir(data_path+str(label_map[gsize])) if not f.startswith(".")]) # don't open system files
		#print(len(maps))
		limited_maps = [i for i in maps if i.startswith(str(7)+"_")]
		#print(limited_maps)

		#print(len(limited_maps))
		#print(str(size)+"_")
		alphabet_sizes= np.arange(2,30)
		percent_correct= []
		
		for alsize in alphabet_sizes:
			num_samples = len(limited_maps)
			num_correct, num_uncallable, num_wrong = 0,0,0
			num_options, num_options_correct, num_options_wrong =0,0,0
			#print("\n")
			#print("alphabet of size: "+str(alsize))
			#print("\n")
			run_offline_phase(als=alsize,map_dir="../data/maps/random/"+str(label_map[gsize]))
	
			for mf in limited_maps:
				patient_map = pickle.load(open("../data/maps/random/"+str(label_map[gsize])+mf,"rb"))
				map_id = "Genome_"+str(int(re.search(r'\d+', mf).group()))
				called, sentinel = run_online_phase(patient_map,als=alsize)
				if sentinel==-1:
					num_uncallable+=1
					num_wrong+=1
				elif sentinel==0:
					if map_id==called:
						num_correct+=1
					else:
						num_wrong+=1
				else:
					num_options+=1
					if map_id==called:
						num_correct+=1
						num_options_correct+=1
					else:
						num_wrong+=1
						num_options_wrong+=1
			score= compute_score(num_samples,num_correct,num_wrong, num_uncallable)
			percent_correct.append(score)
			print("Algorithm Called "+str(score)+ " percent of the callable instances correctly.")
			print(str(num_uncallable)+" samples were considered uncallable.")
			print(str(num_options)+" of the samples had more than one choice at calling time.")
			print("Of these "+ str((num_options_correct/num_options)*100.0) + " were called correctly.")
			print("\n")
	plot_x_vs_y(alphabet_sizes,gsize_percentages,labs=labels,fig_ext="AlphSize_sgrna_size_"+str(size),title="Performance vs. Alphabet Size for sgrna Size"+str(size))