import React, {useEffect} from 'react';
import {useSelector} from 'react-redux';
import {StatusBar, View, TouchableOpacity} from 'react-native';

import {navigationRef} from '~/services/navigation';

//import MaterialCommunityIcons from "react-native-vector-icons/MaterialCommunityIcons";
import colors from '~/styles/colors';

import {NavigationContainer} from '@react-navigation/native';
import {createDrawerNavigator} from '@react-navigation/drawer';
import {createStackNavigator} from '@react-navigation/stack';

//MaterialCommunityIcons.loadFont();

const Stack = createStackNavigator();
const Drawer = createDrawerNavigator();

//Driver
import DriverDrawer from './components/driver/Drawer';
import DriverMap from './screens/Driver/Map';

//Passenger
import PassengerDrawer from './components/passenger/Drawer';
import PassengerMap from './screens/Passenger/Map';

export default function Routes() {
  const showDrawer = false;
  const userType = 'driver'; //possible values: "driver" || "passenger"

  return (
    <>
      <StatusBar backgroundColor={colors.primaryColor} />
      <NavigationContainer ref={navigationRef}>
        {userType === 'driver' && (
          <Drawer.Navigator
            drawerStyle={{width: !showDrawer ? null : 350}}
            initialRouteName="Map"
            drawerContent={(props) => (
              <DriverDrawer
                activeItemIndex={props.state.index}
                navigation={props.navigation}
              />
            )}>
            <Stack.Screen name="Map" component={DriverMap} />
          </Drawer.Navigator>
        )}

        {userType === 'passenger' && (
          <Drawer.Navigator
            drawerStyle={{width: !showDrawer ? null : 350}}
            initialRouteName="Map"
            drawerContent={(props) => (
              <PassengerDrawer
                activeItemIndex={props.state.index}
                navigation={props.navigation}
              />
            )}>
            <Stack.Screen name="Map" component={PassengerMap} />
          </Drawer.Navigator>
        )}
      </NavigationContainer>
    </>
  );
}
