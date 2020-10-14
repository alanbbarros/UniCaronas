import styled from 'styled-components/native';
import colors from '~/styles/colors';

export const Container = styled.ScrollView`
  width: 280px;
  padding: 15px;
  background-color: ${colors.primaryColor};
`;

export const NavigationButton = styled.TouchableOpacity`
  width: 100%;
  background-color: ${(props) =>
    props.active ? colors.primaryColor : `${colors.white}11`};
  height: 60px;
  border-radius: 10px;
  margin-top: 10px;
  flex-direction: row;
  justify-content: space-between;
  padding: 0 15px;
  align-items: center;
`;

export const NavigationButtonText = styled.Text`
  font-size: 18px;
  color: ${colors.white};
`;
