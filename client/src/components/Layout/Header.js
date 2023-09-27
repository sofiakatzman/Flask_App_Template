import React, {useContext} from 'react';
import { UserContext } from '../../functionality/UserContext';
import Navigation from './Navigation/Navigation';


const Header = () => {
  const { user } = useContext(UserContext) || { user: null };

  return (
    <header className="">
      * this space is for header element *
      <Navigation />
    </header>
  )
}


export default Header;