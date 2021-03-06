server.workspace('DQMQuality', 0, 'Summaries', 'Summary')
server.workspace('DQMSummary', 1, 'Summaries', 'Reports')
server.workspace('DQMShift',   2, 'Summaries', 'Shift')
server.workspace('DQMContent', 3, 'Summaries', 'Everything', '^', '^')

server.workspace('DQMContent', 10, 'Data', 'Tk' , '^(Tk/|Pixel|SiStrip|Tracking)', 'DataLayouts/Tk',
                 'DataLayouts/Tk/01 - TEC-',
                 'DataLayouts/Tk/02 - TEC+',
                 'DataLayouts/Tk/03 - TIB',
                 'DataLayouts/Tk/04 - TID-',
                 'DataLayouts/Tk/05 - TID+',
                 'DataLayouts/Tk/06 - TOB',
                 'DataLayouts/Tk/07 - Pixel RecHits Barrel',
                 'DataLayouts/Tk/08 - Pixel RecHits Endcap',
                 'DataLayouts/Tk/09 - Pixel Occupancy',
                 'DataLayouts/Tk/10 - Pixel Clusters Barrel',
                 'DataLayouts/Tk/11 - Pixel Clusters Endcap'
                 )

server.workspace('DQMContent', 11, 'Data', 'Ecal' , '^Ecal.*/', 'DataLayouts/Ecal',
        'DataLayouts/Ecal/04 Ecal Spectrum',
        'DataLayouts/Ecal/00 Number of Ecal RecHits',
        'DataLayouts/Ecal/08 Ecal Timing')
server.workspace('DQMContent', 12, 'Data', 'Hcal' , '^Hcal/', '')
server.workspace('DQMContent', 13, 'Data', 'DT' , '^DT/', '')
server.workspace('DQMContent', 14, 'Data', 'CSC' , '^CSC/', '')
server.workspace('DQMContent', 15, 'Data', 'RPC' , '^RPC/', '')
server.workspace('DQMContent', 16, 'Data', 'Tracking' , '^Tracking/', '')
server.workspace('DQMContent', 17, 'Data', 'L1T', '^L1T/', '')
server.workspace('DQMContent', 18, 'Data', 'L1TEMU', '^L1TEMU/', '')
server.workspace('DQMContent', 19, 'Data', 'HLT', '^HLT/', '')
server.workspace('DQMContent', 20, 'Data', 'Electron' , '^Electron/', '')
server.workspace('DQMContent', 21, 'Data', 'Photon' , '^Photon/', '')
server.workspace('DQMContent', 22, 'Data', 'Muon' , '^Muon/', '')
server.workspace('DQMContent', 23, 'Data', 'Jet' , '^Jet/', '')
server.workspace('DQMContent', 24, 'Data', 'MET' , '^MET/', '')
server.workspace('DQMContent', 25, 'Data', 'BTag' , '^BTag/', '')
server.workspace('DQMContent', 26, 'Data', 'Tau' , '^Tau/', '')
server.workspace('DQMContent', 26, 'Data', 'PFlow' , '^ParticleFlow/', '')

server.workspace('DQMContent', 30, 'Monte Carlo', 'MC Tk' , '^(Tk/|TrackerDigisV|TrackerHitsV|TrackerRecHitsV|Pixel|SiStrip|Tracking)', 'MCLayouts/Tk',
                 'MCLayouts/Tk/01 - TrackerDigisV',
                 'MCLayouts/Tk/02 - TrackerHitsV',
                 'MCLayouts/Tk/03 - TrackerRecHitsV',
                 'MCLayouts/Tk/04 - TrackingMCTruth',
                 'MCLayouts/Tk/05 - TrackingRecHits'
                 )
server.workspace('DQMContent', 31, 'Monte Carlo', 'MC Ecal' , '^Ecal.*/', 'MCLayouts/Ecal')
server.workspace('DQMContent', 32, 'Monte Carlo', 'MC Hcal' , '^Hcal/', '')
server.workspace('DQMContent', 33, 'Monte Carlo', 'MC DT' , '^DT/', '')
server.workspace('DQMContent', 34, 'Monte Carlo', 'MC CSC' , '^CSC/', '')
server.workspace('DQMContent', 35, 'Monte Carlo', 'MC RPC' , '^RPC/', '')
server.workspace('DQMContent', 36, 'Monte Carlo', 'MC Tracking' , '^Tracking/', '')
server.workspace('DQMContent', 37, 'Monte Carlo', 'MC L1T', '^L1T/', '')
server.workspace('DQMContent', 38, 'Monte Carlo', 'MC L1TEMU', '^L1TEMU/', '')
server.workspace('DQMContent', 39, 'Monte Carlo', 'MC HLT', '^HLT/', '')
server.workspace('DQMContent', 40, 'Monte Carlo', 'MC Electron' , '^Electron/', '')
server.workspace('DQMContent', 41, 'Monte Carlo', 'MC Photon' , '^Photon/', '')
server.workspace('DQMContent', 42, 'Monte Carlo', 'MC Muon' , '^Muon/', '')
server.workspace('DQMContent', 43, 'Monte Carlo', 'MC Jet' , '^Jet/', '')
server.workspace('DQMContent', 44, 'Monte Carlo', 'MC MET' , '^MET/', '')
server.workspace('DQMContent', 45, 'Monte Carlo', 'MC BTag' , '^BTag/', '')
server.workspace('DQMContent', 46, 'Monte Carlo', 'MC Tau' , '^Tau/', '')
server.workspace('DQMContent', 47, 'Monte Carlo', 'MC PFlow' , '^ParticleFlow/', 'MCLayouts/PFlow',
                 'MCLayouts/PFlow/01 - Jet Pt Resolution - Barrel',
                 'MCLayouts/PFlow/02 - Jet Pt Resolution - Endcap',
                 'MCLayouts/PFlow/03 - Jet Pt Resolution distribution - Barrel',
                 'MCLayouts/PFlow/04 - Jet Pt Resolution distribution - Endcap',
                 )
