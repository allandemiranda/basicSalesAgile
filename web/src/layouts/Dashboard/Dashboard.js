import React, { Suspense, useEffect, useState } from 'react';
import { renderRoutes } from 'react-router-config';
import PropTypes from 'prop-types';
import { makeStyles } from '@material-ui/styles';
import { LinearProgress } from '@material-ui/core';
import { useSelector } from 'react-redux';
import { NavBar, TopBar, FooterBar } from './components';
import axios from 'utils/axios';
import { useDispatch } from 'react-redux';
import { logout } from 'actions';
import useRouter from 'utils/useRouter';

const useStyles = makeStyles(() => ({
  root: {
    height: '100%',
    width: '100%',
    display: 'flex',
    flexDirection: 'column',
    overflow: 'hidden'
  },
  topBar: {
    zIndex: 2,
    position: 'relative'
  },
  container: {
    display: 'flex',
    flex: '1 1 auto',
    overflow: 'hidden'
  },
  navBar: {
    zIndex: 3,
    width: 256,
    minWidth: 256,
    flex: '0 0 auto'
  },
  content: {
    overflowY: 'auto',
    flex: '1 1 auto'
  }
}));

const Dashboard = props => {
  const { route } = props;
  const router = useRouter();
  const dispatch = useDispatch();

  const session = useSelector((state) => state.session);

  useEffect(()=>{
    if(session.token){
      axios.get('/user/'+ session.user.id, {
        headers: {
          Authorization: 'Bearer ' + session.token,
        }
      }).catch(()=>{
        dispatch(logout(router));
      })
    } else {
      dispatch(logout(router));
    }
  },[session.token, dispatch, router, session.user.id])

  const classes = useStyles();
  const [openNavBarMobile, setOpenNavBarMobile] = useState(false);

  const handleNavBarMobileOpen = () => {
    setOpenNavBarMobile(true);
  };

  const handleNavBarMobileClose = () => {
    setOpenNavBarMobile(false);
  };

  return (
    <div className={classes.root}>
      <TopBar
        className={classes.topBar}
        onOpenNavBarMobile={handleNavBarMobileOpen}
      />
      <div className={classes.container}>
        <NavBar
          className={classes.navBar}
          onMobileClose={handleNavBarMobileClose}
          openMobile={openNavBarMobile}
        />
        <main className={classes.content}>
          <Suspense fallback={<LinearProgress />}>
            {renderRoutes(route.routes)}
          </Suspense>
        </main>
      </div>
      <FooterBar/>
    </div>
  );
};

Dashboard.propTypes = {
  route: PropTypes.object
};

export default Dashboard;
