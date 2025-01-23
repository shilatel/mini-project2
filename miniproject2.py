import pandas as pd
import numpy as np

# Function to add values from a trial to the cumulative sum for a finger
def sum_raw(raw, values): 
     for i, (v,) in enumerate(values):
          raw[i] += v # Add each value to the corresponding index in the raw array


def calc_mean_erp (trial_points, ecog_data):
     ecog_data=pd.read_csv(ecog_data)
     trial_points= pd.read_csv(trial_points)
     # Ensure all trial points are integers
     for col in trial_points.columns:
          trial_points[col]=trial_points[col].astype(int)

     # Initialize a 5x1201 matrix for ERP values and a count for each finger
     fingers_erp_mean=np.zeros((5,1201))
     fingers_count=[0,0,0,0,0]  # Count of trials for each finger

     # Process each trial
     for start_point, peak_point, finger_number in trial_points.values:
          fingers_count[finger_number - 1] += 1 # Increment the trial count for the current finger

          valuse = ecog_data.values[start_point-200:start_point+1001] # Extract the 1201-point window around the trial's start point
          sum_raw(fingers_erp_mean[finger_number - 1], valuse)
     # Calculate the mean ERP for each finger by dividing by the trial count
     for i, finger_action_count in enumerate(fingers_count):
          fingers_erp_mean[i] /= finger_action_count
     
     return fingers_erp_mean


c=calc_mean_erp(r'mini_project_2_data\events_file_ordered.csv',r'mini_project_2_data\brain_data_channel_one.csv' )
print(c)