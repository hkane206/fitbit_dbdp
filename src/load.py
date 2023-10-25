import pandas as pd
import os
import glob

class Load:
    
    def __init__(self, file_path):
        """
        Initialize FitBit object and load all data.

        Parameters
        ----------
        file_path : str
            The path to the folder containing all data collected from FitBit.

        Returns
        -------
        FitBit
            An instance of the FitBit class, with the following DataFrames loaded:
            self.sleep
            self.energy
            self.steps
            self.distance
            self.oxygen
            self.resting_heart_rate
            self.heart_rate
            self.respiration_rate
            self.sleep_stage
            self.floors_climbed
        """

        self.file_path = file_path

        self.sleep = self.load_and_concat("Global Export Data/sleep-*.json")
        self.energy = self.load_and_concat("Global Export Data/calories-*.json")
        self.steps = self.load_and_concat("Global Export Data/steps-*.json")
        self.distance = self.load_and_concat("Global Export Data/distance-*.json")
        self.oxygen = self.load_and_concat("Global Export Data/estimated_oxygen_variation-*.json")
        self.resting_heart_rate = self.load_and_concat("Global Export Data/resting_heart_rate-*.json")
        self.heart_rate = self.load_and_concat("Global Export Data/heart_rate-*.json")
        self.respiration_rate = self.load_and_concat("Global Export Data/distance-*.json")
        self.sleep_stage = self.load_and_concat("Global Export Data/sleep-*.json")
        self.floors_climbed = self.load_and_concat("Global Export Data/altitude-*.json")
    
    def load(self,file_path):
        """
        Load data from a specified file path.
        
        Args:
            file_path (str): The path to the data file.
        
        Returns:
            df (pd.DataFrame): The loaded data as a pandas DataFrame.
        """
        
        self.file_path = file_path
        if os.path.exists(self.file_path):
            file = self.file_path.split('/')[-1]
            file_name, file_format = file.split('.')

            if file_format == 'csv':
                print(f"CSV data loaded from {self.file_path}")
                df = pd.read_csv(self.file_path)
                return df

            elif file_format == 'json':
                print(f"JSON data loaded from {self.file_path}")
                df = pd.read_json(self.file_path)
                return df

            else:
                print(f"Unsupported file format: {file_format}")
                
        else:
            print(f"The path {self.file_path} does not exist.")
    
    def load_and_concat(self, pattern):
        file_paths = glob.glob(os.path.join(self.file_path, pattern))
        data_frames = []
        for file_path in file_paths:
            df = self.load(file_path)
            if df is not None:
                data_frames.append(df)
        if data_frames:  # Check if there are DataFrames to concatenate
            return pd.concat(data_frames, ignore_index=True)
        else:
            return pd.DataFrame()  # Return an empty DataFrame if no data was found
