import React, { useState, useEffect } from 'react';
import { makeStyles } from '@material-ui/styles';
import { Grid } from '@material-ui/core';
import { Page, Header, ListUsers } from 'components';
import axios from 'utils/axios';
import { useSelector } from 'react-redux';

const useStyles = makeStyles(theme => ({
  root: {
    padding: theme.spacing(3)
  },
  container: {
    '& > *': {
      height: '100%'
    }
  }
}));

const DashboardAnalytics = () => {
  const classes = useStyles();
  const session = useSelector((state) => state.session);

  const [users, setUsers] = useState([]);

  useEffect(() => {
    let mounted = true;

    const fetchUsers = () => {
      axios.get('/users/', {
        headers: {
          Authorization: 'Bearer ' + session.token,
        }
      }).then(response => {
        if (mounted) {
          setUsers(response.data.users);
        }
      });
    };

    fetchUsers();

    return () => {
      mounted = false;
    };
  }, []);

  return (
    <Page
      className={classes.root}
      title="Users List"
    >
      <Header
        titleName="List"
        titleSecond="Users"
      />
      <Grid
        className={classes.container}
        container
        spacing={3}
      >   
        <Grid
          item
          lg={12}
          xs={12}
        >
          {users && 
          <ListUsers
            title="All Users"
            users={users}
          />} 
        </Grid>        
      </Grid>
    </Page>
  );
};

export default DashboardAnalytics;
