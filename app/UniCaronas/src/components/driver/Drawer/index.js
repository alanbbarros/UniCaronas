import React from 'react';

import {Container, NavigationButton, NavigationButtonText} from './styles';

export default function Drawer({activeItemIndex, navigation}) {
  return (
    <Container>
      <NavigationButton
        onPress={() => {
          navigation.navigate('Map');
          navigation.closeDrawer();
        }}
        active={activeItemIndex === 0}>
        <NavigationButtonText active={activeItemIndex === 0}>
          Mapa
        </NavigationButtonText>
        {/* <Icon active={activeItemIndex === 0} name="map-marker-radius" /> */}
      </NavigationButton>
    </Container>
  );
}
