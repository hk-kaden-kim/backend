gcs_uri_wav = {
    "biz-meeting":  ["gs://talking-dataset/biz-meeting/biz-result-oup-brainstorming-meeting_16k.wav",
                     "gs://talking-dataset/biz-meeting/biz-result-oup-participating-in-meetings-1_16k.wav",
                     "gs://talking-dataset/biz-meeting/biz-result-oup-participating-in-meetings-2_16k.wav",
                     "gs://talking-dataset/biz-meeting/biz-result-oup-team-meeting_16k.wav"],

    "debating":     ["gs://talking-dataset/debating/2012-first-debate-biden-ryan_16k.wav",
                     "gs://talking-dataset/debating/2012-first-debate-obama-romney_16k.wav",
                     "gs://talking-dataset/debating/captain-america-civil-war_16k.wav",
                     "gs://talking-dataset/debating/lalaland_16k.wav",
                     "gs://talking-dataset/debating/marriage-story_16k.wav",
                     "gs://talking-dataset/debating/midnight-mass-great_16k.wav"],

    "interview":    ["gs://talking-dataset/interview/Robin_Steinberg_16k.wav",
                     "gs://talking-dataset/interview/Sam_Harris_16k.wav",
                     "gs://talking-dataset/interview/Elizabeth_Gilbert_16k.wav",
                     "gs://talking-dataset/interview/Ken_Robinson_16k.wav",
                     "gs://talking-dataset/interview/Dalia_Mogahed_16k.wav"],

    "monologue":    ["gs://talking-dataset/monologue/TL_1203_prostitution_con_opening_JL_16k.wav",
                     "gs://talking-dataset/monologue/JL_1163_cocaleaf_con_opening_TL_16k.wav",
                     "gs://talking-dataset/monologue/DJ_221_ban-gambling_con_opening_YBA_16k.wav",
                     "gs://talking-dataset/monologue/DJ_1203_prostitution_con_opening_TL_16k.wav",
                     "gs://talking-dataset/monologue/EH_2108_surrogacy_con_opening_JL_16k.wav"], 
               }

speaker = {
    "biz-meeting":  
                    [{"min_max" : (2, 6), "speakers" : ['Anna', 'David', 'Maja', 'Marcus', 'Paul', 'Sally']},
                     {"min_max" : (2, 4), "speakers" : ['Anna', 'David', 'Maja', 'Marcus']},
                     {"min_max" : (2, 4), "speakers" : ['Anna', 'David', 'Maria', 'Paul']},
                     {"min_max" : (2, 3), "speakers" : ['Karina', 'Maria', 'Paul']},],

    "debating":     
                     [{"min_max" : (2, 3), "speakers" : ['BIDEN', 'RADDATZ', 'RYAN']},
                     {"min_max" : (2, 3), "speakers" : ['LEHRER', 'OBAMA', 'ROMNEY']},
                     {"min_max" : (2, 7), "speakers" : ['Maximoff', 'Rhodes', 'Rogers', 'Romanoff', 'Stark', 'Vision', 'Wilson']},
                     {"min_max" : (2, 2), "speakers" : ['MIA', 'SEBASTIAN']},
                     {"min_max" : (2, 2), "speakers" : ['CHARLIE', 'NICOLE']},
                     {"min_max" : (2, 2), "speakers" : ['HASSAN', 'KEANE']},],

    "interview":    
                     [{"min_max" : (2, 2), "speakers" : ['Chris', 'Robin']},
                     {"min_max" : (2, 2), "speakers" : ['Chris', 'Sam']},
                     {"min_max" : (2, 2), "speakers" : ['Chris', 'Elizabeth']},
                     {"min_max" : (2, 2), "speakers" : ['Chris', 'Ken']},
                     {"min_max" : (2, 2), "speakers" : ['Chris', 'Dalia']},],

    "monologue":    
                     [{"min_max" : (1, 1), "speakers" : ['John']},
                     {"min_max" : (1, 1), "speakers" : ['Daniel']},
                     {"min_max" : (1, 1), "speakers" : ['Tyler']},
                     {"min_max" : (1, 1), "speakers" : ['Daniel']},
                     {"min_max" : (1, 1), "speakers" : ['Elliot']},],
               }