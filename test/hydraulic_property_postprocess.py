# calculate extended hydraulic properties from the basic properties
# derived from CatchHydroGeo
# Yan Y. Liu <yanliu@illinois.edu>
# 10/31/2016

import pandas as pd
import sys

# usage: python thisscript hydroprop.csv 0.05 hydropropfull.csv
def main():
    hydropropotxt = str(sys.argv[1])
    manning_n = str(sys.argv[2])
    handpropotxt = str(sys.argv[3])
    df_result = pd.read_csv(hydropropotxt)
    df_result['Roughness'] = float(manning_n)
    #df_result = df_result.drop('COMID', 1)
    df_result = df_result.rename(columns=lambda x: x.strip(" "))
    df_result['TopWidth (m)'] = df_result['SurfaceArea (m2)']/df_result['LENGTHKM']/1000
    df_result['WettedPerimeter (m)'] = df_result['BedArea (m2)']/df_result['LENGTHKM']/1000
    df_result['WetArea (m2)'] = df_result['Volume (m3)']/df_result['LENGTHKM']/1000
    df_result['HydraulicRadius (m)'] = df_result['WetArea (m2)']/df_result['WettedPerimeter (m)']
    df_result['HydraulicRadius (m)'].fillna(0, inplace=True)
    df_result['Discharge (m3s-1)'] = df_result['WetArea (m2)']* \
    pow(df_result['HydraulicRadius (m)'],2.0/3)* \
    pow(df_result['SLOPE'],0.5)/df_result['Roughness']
    df_result.to_csv(handpropotxt,index=False)


if __name__ == "__main__":
    main()
