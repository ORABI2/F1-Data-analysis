import matplotlib.pyplot as plt
import fastf1
import fastf1.plotting


# enable some matplotlib patches for plotting timedelta values and load
# FastF1's default color scheme
fastf1.plotting.setup_mpl(misc_mpl_mods=False)
# load a session and its telemetry data
session = fastf1.get_session(2022, 'Spanish Grand Prix', 'R')
# Loading the session 
session.load()
# getting the fastes lap for max verstappen
ver_lap = session.laps.pick_driver('VER').pick_fastest()
# getting the fastes lap for lewis hamilton
ham_lap = session.laps.pick_driver('HAM').pick_fastest()

# getting the ditance
ver_tel = ver_lap.get_car_data().add_distance()
ham_tel = ham_lap.get_car_data().add_distance()

# getting the color themes for each team to assign to the driver
rbr_color = fastf1.plotting.team_color('RBR')
mer_color = fastf1.plotting.team_color('MER')

# visualizing...
fig, ax = plt.subplots()
ax.plot(ver_tel['Distance'], ver_tel['Speed'], color = rbr_color, label = 'VERSTAPPEN')
ax.plot(ham_tel['Distance'], ham_tel['Speed'], color = mer_color, label = 'HAMILTON')

ax.set_xlabel('Distance in m')
ax.set_ylabel('Speed in km/h')

ax.legend()
plt.suptitle(f"Fastest lap comparison \n"
             f"{session.event['EventName']} {session.event.year} Race")


plt.show()
