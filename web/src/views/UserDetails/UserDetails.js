import React, { useState, useEffect } from 'react';
import { makeStyles } from '@material-ui/styles';
import { Grid } from '@material-ui/core';
import PropTypes from 'prop-types';
import axios from 'utils/axios';
import { Page, Header } from 'components';
import { LatestProducts, ProfileDetails} from './components';
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

const UserDetails = (props) => {
  const { match } = props;
  const classes = useStyles();
  const { id } = match.params;
  const session = useSelector((state) => state.session);

  const [user, setUser] = useState({});

  useEffect(() => {
    let mounted = true;
    const fetchUser = () => {
      axios.get('/user/' + id, {
        headers: {
          Authorization: 'Bearer ' + session.token,
        }
      }).then(response => {
        if (mounted) {
          setUser(response.data.user);
        }
      });
    };

    fetchUser();

    return () => {
      mounted = false;
    };
  }, [id, session.token]);

  const [sales, setSales] = useState(0.00);
  useEffect(() => {
    let mounted = true;

    const fetchSales = () => {
      axios.get('/user/'+ id +'/sales/').then(response => {
        if (mounted) {
          const data = response.data.sales
          const arrSum = function(arr){
            return arr.reduce(function(a,b){
              return a + b.total
            }, 0);
          }
          setSales(parseFloat(arrSum(data).toFixed(2)));
        }
      });
    };

    fetchSales();

    return () => {
      mounted = false;
    };
  }, [id]);

  return (
    <Page
      className={classes.root}
      title="Analytics Dashboard"
    >
      <Header
        titleName="Details"
        titleSecond="User"
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
          <ProfileDetails
            profile={user}
            sales={sales}
          />
        </Grid>      
        <Grid
          item
          lg={12}
          xs={12}
        >
          <LatestProducts id={parseInt(id)}/>
        </Grid>
        
      </Grid>
    </Page>
  );
};

UserDetails.propTypes = {
  history: PropTypes.object.isRequired,
  match: PropTypes.object.isRequired
};

export default UserDetails;
